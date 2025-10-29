from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "textutils-2.html")



def space_remover(request):
    return HttpResponse("This is the space remover page.")

def capitalize(request):
    return HttpResponse("This is the capitalize page.")

def remove_punctuation(request):
    input_text = request.POST.get('text', 'default')
    remove_punctuation = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('fullcaps', 'off')
    space_remover = request.POST.get('spaceRemover', 'off')

    # Track if any operation was selected
    operation_done = False

    if remove_punctuation == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        input_text = "".join(char for char in input_text if char not in punctuations)
        operation_done = True

    if capitalize == "on":
        input_text = input_text.upper()
        operation_done = True

    if space_remover == "on":
        analyzed = ""
        for idx in range(len(input_text)):
            if not (input_text[idx] == " " and idx + 1 < len(input_text) and input_text[idx + 1] == " "):
                analyzed += input_text[idx]
        input_text = analyzed
        operation_done = True

    # If no operation was chosen
    if not operation_done:
        return HttpResponse("⚠️ Please select at least one operation and try again.")

    # Final result
    user_output = {
        'purpose': 'Text Processed Successfully',
        'analyzed_text': input_text
    }

    return render(request, "analyzed.html", user_output)
