describe("Header Info Test", () => {
    it("Visits home URL and ensures <h1> is correct", () => {
        cy.visit('/')
        cy.get('h1').should('contain', 'Vite + React');
    });
    it("Ensures count button default value is correct", () => {
        cy.visit('/')
        cy.get('#countButton').should('contain', 'count is 0');
    });
})