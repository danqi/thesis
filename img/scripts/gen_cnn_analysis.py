from pylab import figure, ylabel, xticks, bar, \
                  legend, savefig, text

from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

groups = ["Exact match", "Paraphrasing", "Partial clue", "Multi. sent.", "Coref. errors", "Hard", "All"]

data = [[100, 95.1, 89.5, 50.0, 37.5, 5.9, 74.0],
        [100, 78.1, 73.7, 50.0, 50.0, 11.8, 66.0]]

figure()
ylabel('Accuracy')

x1 = [2.0 + 10.0 * k for k in range(7)]

xticks([x + 0.75 for x in x1], groups)

width = 2.5
bar(x1, data[0], width=width, color="#56B4E9", label="Stanford Attentive Reader", edgecolor='k')
bar([x + width for x in x1], data[1], width=width, color="#E69F00", label="Feature-based Classifier", edgecolor='k')
# bar([x + 1.0 for x in x1], data[2], width=0.45, color="#94c6da", label="WebQuestions", edgecolor='k')
# bar([x + 1.5 for x in x1], data[3], width=0.45, color="#1770ab", label="WikiMovies", edgecolor='k')

for j in range(len(data[0])):
    text(x1[j] - 1.5, data[0][j] + 0.75, str(data[0][j]))

for j in range(len(data[1])):
    text(x1[j] + width - 1.0, data[1][j] + 0.75, str(data[1][j]))

legend()
savefig('barplot.png')
