from minicolumn import MiniColumn

sentence = "good morning"

source_files = ["chat.0.txt", "chat.1.txt", "chat.2.txt"]

mcol = MiniColumn(source_files, "tests/data")

predicts = mcol.evaluate(sentence)


def get_hits(predicts):
    hits = []
    for predict in predicts:
        hit = {}
        predict.reverse()
        hit['convo'] = predict[0][0]['convo'][0]
        sent = [] 
        start, end = 0, 1
        for node in predict:
            start = node[start]['start']
            end = node[end - 1]['end']
        for obj in predict[2][start:end]:
            sent.append(obj['words'][0][0])
        hit['words'] = " ".join(sent)

        hits.append(hit)

    return hits


print(get_hits(predicts))
