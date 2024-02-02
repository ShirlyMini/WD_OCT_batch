Feature: NopCommerce Login to Dashbord

  Scenario: Login and verify Dashbord
    Given : Launch Browser
    When : Open Nopcommerce page
    And : Enter Username "admin@yourstore.com" and Password "admin"
    And : Click Submit
    Then : verify the presence of Dashboard Logo


