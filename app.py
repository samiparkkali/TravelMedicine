from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'alegria'

questions = [
    {
        'id': 1,
        'question': 'Qual das vacinas não é precisa para uma viagem à Ásia?',
        'options': ['Hepatite A', 'Febre Tifóide', 'Febre Amarela', 'Encefalite Japonesa'],
        'correct_answer': 'Febre Amarela'
    },
    {
        'id': 2,
        'question': 'Qual é a doença mais frequente num viajante?',
        'options': ['Malária', 'Diarreia do Viajante', 'Dengue', 'Hepatite B'],
        'correct_answer': 'Diarreia do Viajante'
    },
    {
        'id': 3,
        'question': 'O que devemos levar sempre connosco numa viagem?',
        'options': ['Um casaco de inverno', 'Um livro grande', 'Um kit de primeiros socorros', 'Muitos sapatos'],
        'correct_answer': 'Um kit de primeiros socorros'
    },
    {
        'id': 4,
        'question': 'Qual é a causa de mortalidade mais comum em viajantes?',
        'options': ['Acidentes de viação', 'Doenças infecciosas', 'Ataques de animais selvagens', 'Afogamento'],
        'correct_answer': 'Acidentes de viação'
    },
    {
        'id': 5,
        'question': 'Se usar protector solar e repelente de insectos, o que devo colocar em primeiro lugar é o repelente.',
        'options': ['Verdadeiro', 'Falso'],
        'correct_answer': 'Falso'
    },
    {
        'id': 6,
        'question': 'A malária pode ser transmitida através do contacto directo com uma pessoa infetada.',
        'options': ['Verdadeiro', 'Falso'],
        'correct_answer': 'Falso'
    },
    {
        'id': 7,
        'question': 'O gelo é uma fonte importante de transmissão de doenças.',
        'options': ['Verdadeiro', 'Falso'],
        'correct_answer': 'Verdadeiro'
    },
    {
        'id': 8,
        'question': 'O vírus do Zika pode ser transmitido através de relações sexuais.',
        'options': ['Verdadeiro', 'Falso'],
        'correct_answer': 'Verdadeiro'
    },
    {
        'id': 9,
        'question': 'Que sintomas uma viagem para altitudes elevadas (>2500m) poderá causar?',
        'options': ['Dor de cabeça', 'Perda de apetite', 'Vómitos', 'Todos os anteriores'],
        'correct_answer': 'Todos os anteriores'
    },
    {
        'id': 10,
        'question': 'Quantas doses de vacina contra a hepatite A são necessárias para uma proteção eficaz?',
        'options': ['Uma dose', 'Duas doses', 'Três doses', 'Quatro doses'],
        'correct_answer': 'Duas doses'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def start_quiz():
    session.clear()
    session['score'] = 0
    session['question_index'] = 0
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    if session['question_index'] >= len(questions):
        return redirect(url_for('results'))

    current_question = questions[session['question_index']]

    if request.method == 'POST':
        user_answer = request.form.get(f'question_{current_question["id"]}')
        if user_answer == current_question['correct_answer']:
            session['score'] += 1  # Incrementa a pontuação se a resposta estiver correta
        session['question_index'] += 1
        return redirect(url_for('question'))
    else:
        return render_template('question.html', question=current_question, question_number=session['question_index'] + 1, total_questions=len(questions))

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(questions)
    return render_template('results.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)