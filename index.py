def calc_dScores(scores: list, answers: list) -> list:
  if(len(scores) != len(answers)):
    return [-1]

  results = []
#positive score indicates the model was correct with its prediction
  for i, score in enumerate(scores):
    if(answers[i] == "0"):
      dScore = score[0] - score[1]
    else:
      dScore = score[1] - score[0]
    results.append(dScore)
  return results

def getScores(classOutput: list) -> list:
  scores = []
  for entry in classOutput:
    scores.append(entry["scores"])
  return scores

def evaluate(input: ps.DataFrame, classOutput: list) -> list:
  answers = input["misconception"]
  scores = getScores(classOutput)
  scoresData = calc_dScores(scores, answers)

