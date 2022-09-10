from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)




f= open("Summary\D0702A.txt").readlines()
f=str(f)
g= open("Gold_summary\D0702Agold1.txt").readlines()
g=str(g)
scores = scorer.score(f,g)
print(scores)
