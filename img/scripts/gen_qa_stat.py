from pylab import figure, ylabel, xticks, bar, \
                  legend, savefig, text

groups = ["Question length", "Answer length"]

data = [
    [10.4, 3.2],
    [7.2, 1.8],
    [6.7, 2.4],
    [7.5, 2.1]
    ]

figure()
ylabel('#tokens')

x1 = [2.0, 5.0]

xticks([x + 0.75 for x in x1], groups)

bar(x1, data[0], width=0.45, color="#c30d24", label="SQuAD", edgecolor='k')
bar([x + 0.5 for x in x1], data[1], width=0.45, color="#cccccc", label="TREC", edgecolor='k')
bar([x + 1.0 for x in x1], data[2], width=0.45, color="#94c6da", label="WebQuestions", edgecolor='k')
bar([x + 1.5 for x in x1], data[3], width=0.45, color="#1770ab", label="WikiMovies", edgecolor='k')

for i in range(len(data)):
    for j in range(len(data[i])):
        text(x1[j] + i * 0.5 - 0.1, data[i][j] + 0.1, str(data[i][j]))

legend()
savefig('barplot.png')
