"""
    Fourth example on:
    https://kristw.github.io/d3kit-timeline/

    Labella.py doesn't implement the full colorscale from d3, just category 10
    and category 20. Below we show an example of implementing specific colors
    based on the input data.
"""

from datetime import date

from labella.timeline import TimelineTex, TimelineSVG


def color(d):
    idx = d['episode']
    if idx == 1:
        return '#000000'
    else:
        return '#1F77B4'


def main():
    items = [
            {'time': date(2016, 11, 1), 'episode': 1,
                'text': 'SQuAD 1.1'},
            {'time': date(2015, 12, 7), 'episode': 1,
                'text': 'CNN/Daily Mail'},
            {'time': date(2016, 5, 2), 'episode': 1,
                'text': 'Children Book Test'},
            {'time': date(2017, 7, 30), 'episode': 1,
                'text': 'TriviaQA'},
            {'time': date(2017, 9, 1), 'episode': 1,
                'text': 'RACE'},
            {'time': date(2018, 5, 1), 'episode': 1,
                'text': 'NarrativeQA'},
            {'time': date(2018, 7, 15), 'episode': 1,
                'text': 'SQuAD 2.0'},
            {'time': date(2018, 11, 2), 'episode': 1,
                'text': 'HotpotQA'},
            {'time': date(2015, 12, 7), 'episode': 2,
                'text': 'Attentive Reader'},
            {'time': date(2016, 8, 7), 'episode': 2,
                'text': 'Stanford Attentive Reader'},
            {'time': date(2017, 4, 24), 'episode': 2,
                'text': 'Match-LSTM'},
            {'time': date(2017, 4, 24), 'episode': 2,
                'text': 'BiDAF'},
            {'time': date(2017, 7, 30), 'episode': 2,
                'text': 'R-Net'},
            {'time': date(2018, 4, 30), 'episode': 2,
                'text': 'QANet'},
            {'time': date(2018, 6, 1), 'episode': 2,
                'text': 'BiDAF+self-att.+ELMo'},
            {'time': date(2018, 10, 11), 'episode': 2,
                'text': 'BERT'},
            ]

    options = {
        'initialWidth': 400,
        'initialHeight': 400,
        'direction': 'right',
        'dotColor': color,
        'labelBgColor': color,
        'linkColor': color,
        'textFn': lambda d: d['text'],
        'margin': {'left': 0, 'right': 0, 'top': 0, 'bottom': 0},
        'layerGap': 20,
        'labella': {
            'maxPos': 1200,
            'algorithm': 'simple'
            }
        }

    tl = TimelineSVG(items, options=options)
    tl.export('timeline.svg')

    tl = TimelineTex(items, options=options)
    tl.export('timeline.tex')


if __name__ == '__main__':
    main()
