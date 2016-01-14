import guessTheNumberUpgrade

def test_randomGenerator():
    assert guessTheNumberUpgrade.generateNumber( 25 ) <= 25
    assert guessTheNumberUpgrade.generateNumber( 5 ) <= 5
    assert guessTheNumberUpgrade.generateNumber( 10 ) <= 10
    assert guessTheNumberUpgrade.generateNumber( 1 ) <= 1
    
def test_evaluate():
    assert guessTheNumberUpgrade.evaluateAnswer( 3, 2 ) == False
    assert guessTheNumberUpgrade.evaluateAnswer( 2, 3 ) == False
    assert guessTheNumberUpgrade.evaluateAnswer( 5, 5 ) == True

