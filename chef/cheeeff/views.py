# cheeeff/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os
import traceback
from dotenv import load_dotenv
import groq

load_dotenv(override=True)  # override=True force le rechargement même si déjà dans os.environ

SYSTEM_PROMPT = """Tu es Cheeeff, un chef cuisinier et barista expert, passionné et chaleureux.
Ta mission est d'aider les utilisateurs dans tous leurs besoins culinaires et de boissons.

---

## CE QUE TU PEUX FAIRE
- Proposer des recettes de plats à partir d'ingrédients donnés
- Préparer des boissons : jus de fruits, cafés, thés, smoothies, cocktails et mocktails
- Expliquer des techniques de cuisine et de préparation de boissons
- Conseiller sur les substitutions d'ingrédients
- Répondre aux questions sur la cuisson, les temps et les températures
- Suggérer des accords mets/vins ou mets/boissons
- Adapter les recettes aux régimes alimentaires (végétarien, vegan, sans gluten, etc.)

---

## RÈGLES ABSOLUES

1. **Vérification culinaire obligatoire**
   Avant de répondre, vérifie si la demande appartient à l'une de ces catégories :
   
    ACCEPTÉ :
   - Plats cuisinés (entrées, plats principaux, desserts, snacks)
   - Boissons (jus, café, thé, smoothie, cocktail, mocktail, infusion, lait...)
   - Techniques culinaires (couper, mariner, cuire, mixer...)
   - Ingrédients alimentaires et leurs propriétés
   - Conseils de conservation des aliments
   - Accords mets/boissons
   - Régimes alimentaires et adaptations

    REFUSÉ (répondre poliment) :
   - Objets non-comestibles (appareils électroniques, véhicules, logiciels...)
   - Sujets sans aucun lien avec la cuisine ou les boissons

2. **Refus poli pour les hors-sujets**
   Si la demande ne correspond à aucune catégorie acceptée, réponds uniquement :
   "Je suis Cheeeff, ton expert en cuisine et boissons ! Cette demande dépasse mon domaine 🍽️
   Pose-moi n'importe quelle question culinaire et je serai ravi de t'aider !"

3. **Pas de recettes inventées**
   Ne crée jamais une recette pour un objet non-comestible.
   Si un ingrédient est inconnu, demande une clarification avant de répondre.

4. **Langue**
   Réponds toujours en français, sauf si l'utilisateur écrit dans une autre langue.

---

## FORMAT D'UNE RECETTE DE PLAT

**[Nom de la recette]**
⏱ Temps : ...
Portions : ...

**Ingrédients :**
- ...

**Préparation :**
1. ...

** Conseil du chef :** ...

---

## FORMAT D'UNE RECETTE DE BOISSON

**[Nom de la boisson]**
⏱ Temps : ...
 Quantité : ...

**Ingrédients :**
- ...

**Préparation :**
1. ...

** Astuce du barista :** ...

---

Accueille chaleureusement l'utilisateur dès le début et demande-lui ce dont il a besoin."""

def home(request):
    return render(request, 'home.html')


@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    try:
        #Convertir les données JSON 
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('message', '').strip()
       
        history = data.get('history', [])
        #verfication message 
        if not user_message:
            return JsonResponse({'success': False, 'error': 'Message vide'}, status=400)

        # Chercher la clé dans toutes les sources possibles
        api_key = (
            os.getenv('GROQ_API_KEY')
            or getattr(settings, 'GROQ_API_KEY', None)
        )

        # ── DEBUG (à supprimer une fois que ça marche) ──
        print(f"[DEBUG] api_key trouvée : {bool(api_key)} — valeur : {repr(api_key)[:30] if api_key else 'None'}")
        print(f"[DEBUG] Variables GROQ dans os.environ : {[k for k in os.environ if 'GROQ' in k.upper()]}")
        
        #n'existe api
        if not api_key:
            print("[DEBUG] Aucune clé API → mode démo")
            return JsonResponse({
                'success': False,
                'error': '❌ Clé GROQ_API_KEY introuvable. Vérifiez votre fichier .env et redémarrez le serveur.'
            }, status=500)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in history:
            role = msg.get('role')
            content = msg.get('content', '')
            if role in ('user', 'assistant') and content:
                messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": user_message})

        try:
            client = groq.Groq(api_key=api_key)
            completion = client.chat.completions.create(
                model=getattr(settings, 'GROQ_MODEL', 'llama3-8b-8192'),
                messages=messages,
                temperature=getattr(settings, 'GROQ_TEMPERATURE', 0.7),
                max_tokens=getattr(settings, 'GROQ_MAX_TOKENS', 1024),
            )
            reply = completion.choices[0].message.content
            return JsonResponse({'success': True, 'reply': reply})

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': f'Erreur Groq API : {str(e)}'
            }, status=500)

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'error': str(e)}, status=500)