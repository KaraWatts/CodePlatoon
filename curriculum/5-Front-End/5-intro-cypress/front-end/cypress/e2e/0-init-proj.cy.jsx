describe('My First Cypress Test', () => {
    it('Visits the app and asserts title', () => {
      cy.visit('/'); // Replace with your app's URL
      cy.get('h1').should('contain', 'Vite + React'); // Adjust the selector and text as needed
    });
  });