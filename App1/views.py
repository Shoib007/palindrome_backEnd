from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

palindromes = [
    "A nut for an jar of tuna",
    "kayak",
    "deified",
    "rotator",
    "repaper",
    "King, and you glad you are king?",
    "deed",
    "peep",
    "wowe",
    "noon",
    "civic",
    "racecar",
    "level",
    "mom",
    "bird rib",
    "taco cat",
    "UFO tofu",
    "Borrow or rob?",
    "Never odd or even.",
    "We panic in a pew.",
    "Won't lovers revolt now?",
    "Ma is a nun, as I am.",
    "Don't nod.",
    "Sir, I demande, I am a maid named Iris.",
    "Was it a car or a cat I saw?",
    "Yo, Baana Boy!",
    "Eva, can I see bees in a cave?",
    "Madam, in Eden, I'm Adam.",
    "A man, a plan, a canal, Panama!",
    "Never a foot too far, even.",
    "Red roses run no risk, sir, on Nurse's order.",
    "He lived as a devil, eh?",
    "Ned, I am a maiden.",
    "Now, sir, a war is won!",
    "Evade me, Dave!",
    "Dennis and Edna sinned.",
    "Step on no pets!"
]


def Home(request):
    return HttpResponse("Its Home")

@api_view(["GET"])
def getPalindrome(request):
    pelendrom = random.sample(palindromes,1)
    return Response({'data':pelendrom})

@api_view(['POST'])
def verifyPalindrome(request):
    string = request.data['string']
    print(string)
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("?","")
    string = string.replace("!","")
    string = string.replace(".","")
    string = string.replace("'","")
    string = string.lower()
    print(f"After Modification : {string}")
    if string == string[::-1]:
        return Response("True")
    else:
        return Response("False")
