Feature: The user can go to Youtube and search for a video

  Scenario: Go to Youtube and search for simple video. Assert that video was found
    Given Go to Youtube
     When Type pokemon last battle vs rival in search input
     Then Click search button
     Then The result page contains video Pokémon Anime BGM - Champion Battle (Last Battle VS Rival) (1997~1998-M79)