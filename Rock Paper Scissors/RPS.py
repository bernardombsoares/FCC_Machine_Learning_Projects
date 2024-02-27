# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[],play_order={}):

    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if not prev_play or len(opponent_history)<=5:
        return "S"
    
    last_five = "".join(opponent_history[-5:])
    if last_five in play_order.keys():
        play_order[last_five]+=1
    else:
        play_order[last_five]=1
   
    potential_plays = [
        last_five[1:] + "R",
        last_five[1:] + "P",
        last_five[1:] + "S",
    ]

    for i in potential_plays:
        if i not in play_order.keys():
            play_order[i]=0

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }
    
    prediction = max(sub_order, key=sub_order.get)[-1:]
    
    return ideal_response[prediction]