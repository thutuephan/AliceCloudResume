// This test is to make sure my API returns an updated value

describe('My First Test', () => {
  it('successfully loads', () => {
    cy.visit('https://alicezenmind.com')

    cy.contains('email').click()
    cy.get("h3")

   
    cy.get('.counter')
    cy.get('#banner')
    
  })

  it('the features on the homepage are correct', () => {
    cy.visit('https://alicezenmind.com')

    // Get an input, type into it and verify
    // that the value has been updated
    cy.get('.navigation')
      .should('exist')
      .contains('GITHUB')
    
  })

  

// "only" keyword will make cypress run only the specific one. If we want to test all, remove the "only" keyword

  it.only('the features on the homepage are correct', () => {
    cy.visit('https://alicezenmind.com')

     
    // Verify that the value has been updated from the database
    cy.get('#fetch')
    cy.get('h3').contains('CERTIFICATIONS') 
  })

})






