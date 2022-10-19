# Cas de test pour créer s'incrire sur l'application

Scenario: S'inscrire sur l'application
    Given I am on "/register"
    When I fill in "Votre nom" with "Jean Dubois"
    And I fill in "Votre pseudo" with "jdubois"
    And I fill in "Votre email" with "jean.dubois@monmail.com"
    And I fill in "Votre mot de passe" with "123456"
    And I fill in "Confirmer votre mot de passe" with "123456"
    And I press "S'inscrire"
    Then I should see "Compte créé avec succès! Vous êtes connecté en tant que Jean Dubois"

## Pages de l'application à tester

- [ ] Page d'incription
  - [ ] charger la page
  - [ ] remplir le formulaire
  - [ ] valider le formulaire
- [ ] Page d'accueil
  - [ ] charger la page
  - [ ] vérifier le titre
  - [ ] vérifier le message de bienvenue
