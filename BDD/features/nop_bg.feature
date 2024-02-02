Feature: NopCommerce Login to Dashbord and check modules

  Background: login to nopcommerce site
    Given : Launch Browser
    When : Open Nopcommerce page
    And : Enter Username "admin@yourstore.com" and Password "admin"
    And : Click Submit
    Then : verify the presence of Dashboard Logo

  Scenario: Login and verify Dashbord
    And : click customer module
    Then : verify customer items

  Scenario: Login and verify Dashbord
      And : click sales module
      Then : verify sales items