# 🍳 Chef-IA

<p align="center">
  <img src="https://img.shields.io/badge/status-actif-success?style=for-the-badge" alt="Statut">
  <img src="https://img.shields.io/badge/IA-OpenAI-blue?style=for-the-badge" alt="IA">
  <img src="https://img.shields.io/badge/licence-MIT-green?style=for-the-badge" alt="Licence">
  <img src="https://img.shields.io/badge/version-1.0.0-orange?style=for-the-badge" alt="Version">
</p>

<p align="center">
  <strong>Une application intelligente de cuisine qui utilise l'intelligence artificielle pour vous aider à créer des recettes personnalisées à partir des ingrédients que vous avez sous la main.</strong>
</p>

## 📖 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Captures d'écran](#-captures-décran)
- [Technologies utilisées](#-technologies-utilisées)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [API Documentation](#-api-documentation)
- [Contribuer](#-contribuer)
- [Licence](#-licence)
- [Contact](#-contact)

## 🎯 À propos

**Chef-IA** est une application innovante qui combine la puissance de l'intelligence artificielle avec l'art culinaire. Que vous soyez un chef expérimenté ou un débutant en cuisine, Chef-IA vous aide à :

- Trouver l'inspiration avec les ingrédients que vous possédez déjà
- Découvrir de nouvelles recettes adaptées à vos préférences alimentaires
- Réduire le gaspillage alimentaire en utilisant intelligemment vos ingrédients
- Gagner du temps dans la planification de vos repas

## ✨ Fonctionnalités

### 🤖 Génération de recettes par IA
- Créez des recettes personnalisées à partir de vos ingrédients disponibles
- Obtenez des instructions détaillées et des conseils de préparation
- Recevez des suggestions de plats adaptés à vos goûts

### 📝 Suggestions d'ingrédients alternatifs
- Remplacez facilement les ingrédients manquants
- Propositions d'alternatives pour les régimes spécifiques
- Adaptations pour les allergies et intolérances

### ⏱️ Temps de préparation estimé
- Estimation précise du temps total de préparation
- Détail du temps de préparation et de cuisson
- Gestion des recettes rapides et élaborées

### 🥗 Adaptation aux régimes alimentaires
- Végétarien et Végétalien
- Sans gluten et Sans lactose
- Cétogène et Paleo
- Halal et Kosher
- Régimes personnalisés

### 📊 Gestion du stock d'ingrédients
- Suivez ce que vous avez dans votre cuisine
- Recevez des alertes quand un ingrédient manque
- Suggestions de recettes basées sur votre stock

## 📸 Captures d'écran

<div align="center">
  <img src="https://github.com/user-attachments/assets/4efa61e5-1e07-4819-b937-7768ab2557d0" alt="Page d'accueil" width="600">
  <br>
  <em>Page d'accueil de l'application</em>
  <br><br>
  <img src="https://github.com/user-attachments/assets/7666c58b-d839-4c9a-91b1-64e2037b642d" alt="Génération de recette" width="600">
  <br>
  <em>Interface de génération de recettes</em>
</div>

## 🛠️ Technologies utilisées

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Node.js / Express.js
- Python / Flask

### Intelligence Artificielle
- OpenAI API (GPT-3.5 / GPT-4)
- Google Gemini

### Base de données
- MongoDB
- PostgreSQL

### Outils de développement
- Git
- Docker
- VS Code

## 🚀 Installation

### Prérequis
- Node.js (v14 ou supérieur) ou Python (v3.8+)
- MongoDB ou PostgreSQL
- Clé API OpenAI

### Étapes d'installation

```bash
# Cloner le repository
git clone https://github.com/islemmimouni/chef-ia.git

# Accéder au dossier
cd chef-ia

# Installer les dépendances backend
cd backend
npm install
# ou pour Python
pip install -r requirements.txt

# Installer les dépendances frontend
cd ../frontend
npm install
