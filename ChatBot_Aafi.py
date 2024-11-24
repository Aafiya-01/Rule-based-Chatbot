import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response("Hello!, Are you ill??", ['hello', 'hi', 'hey', 'heyo'], single_response=True)
    response("I'm sorry to hear that 🙁, Tell me about your symptoms", [ "i ","am ","sick","ill","yes"],required_words=["sick","ill","yes"],single_response=True)
    response("Thank you for coming here you should consult a Doctor ASAP !!",["no"],required_words=["no"], single_response=True)
    response("Common cold! suggested medication: afrin, robafen ",["pain","in","muscles","sneezing","running ","nose"],required_words=["sneezing","running ","nose"],single_response=True)
    response("Malaria! suggested medication: atovaquone, proguanil",["pain","in","abdomen","nausea","fever","sweating","vomiting"], required_words=["nausea","sweating","vomiting"],single_response=True)
    response("Headache! suggested medication: paracetamol, asprin",["headache"],required_words=["headache"], single_response=True)
    response("Typhoid fever!! suggested medication: IV fluids and ORS",["bloating","constipation","diarrhoea","appetite"], required_words=["bloating","constipation","diarrhoea","appetite"],single_response=True)
    response("Mention Not! That's my job",["thanks","thank", "you","your","help"], required_words=["thanks","thank", "you","your","help"],single_response=True)


    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
