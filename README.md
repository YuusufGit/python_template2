## How to Run
1. Make sure you have Python 3.12.7 installed on your system because that's what I used.
2. Clone this repository to your local machine: https://github.com/YuusufGit/python_template2.git

3. Go to the `src` directory:

4. Run the program: python planetgame.py

Here's a mermaid flowchart to help out:
---------------------------------------------------------------
graph TD
    A[Roll Functions] -->|Dice Roll| B[Rolltaketwo Function]
    B -->|Generates Value| C[Planetary Characteristics]
    
    C -->|Set Characteristics| D[Size]
    C -->|Set Characteristics| E[Atmosphere]
    C -->|Set Characteristics| F[Water]
    C -->|Set Characteristics| G[Population]
    C -->|Set Characteristics| H[Starport]
    C -->|Set Characteristics| I[Government]
    C -->|Set Characteristics| J[Law_Level]
    C -->|Set Characteristics| K[Tech_Level]
    C -->|Set Characteristics| L[Planetoid]
    C -->|Set Characteristics| M[Gas_Presence]
    
    D -->|Affects| E
    E -->|Affects| F
    F -->|Affects| G
    G -->|Affects| H
    H -->|Affects| I
    I -->|Affects| J
    J -->|Affects| K
    K -->|Affects| L
    L -->|Affects| M

    subgraph Modifier Calculation
        O[Tech Modifier Calculation] --> P[Starport, Size, Atmosphere, Water, Population, Government]
    end

    subgraph Trait Roll Functions
        B --> Q[Water Roll]
        B --> R[Population Roll]
        B --> S[Tech_Level Roll]
    end
    
    subgraph Determining Special Features
        T[Base Features] --> U[Naval, Scout, PirateBase]
        T --> V[Gas_Presence]
        T --> W[Trade Codes]
    end

    subgraph Output
        X[Planetary Information Output]
        X --> Y[Trade Codes, Starport, Tech Level, Water, Population, Government]
    end
---------------------------------------------------------------

Brief overview: The game asks the user for a name and generates a planet based on that seed. Each time you rerun the program with the same name
It produces the same results because it's the same seed.

The code is really just made up of a bunch of functions and if statements used to make each characteristic of the planet.

Based off of the cepheus game <: :>
                                M

Additional stuff I added:
I tweaked some things in the output of the game because the instructions weren't clear on the cepheus game rules. The things I changed are Polities and world alliance,
Communication routes and trade routes

