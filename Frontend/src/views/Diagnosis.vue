<template>
    <div class="container">
      <h1>Mental Health Quiz</h1>
      <form @submit.prevent="calculateResults">
        <div v-for="(question, index) in questions" :key="index" class="question">
          <label>{{ index + 1 }}. {{ question.text }}</label><br>
          <div v-for="option in question.options" :key="option.value">
            <input type="radio" :name="'q' + (index + 1)" :value="option.value" v-model="answers[index]"> {{ option.text }}<br>
          </div>
        </div>
        <button type="submit">Submit</button>
      </form>
      <div v-if="results.length" class="result">
        <h2>Top 5 Potential Conditions</h2>
        <ol>
          <li v-for="result in results" :key="result.name">{{ result.name }}: {{ result.score }}</li>
        </ol>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MentalHealthQuiz',
    data() {
      return {
        questions: [
          {
            text: 'How often do you feel sad or depressed?',
            options: [
              { text: 'Never', value: 1 },
              { text: 'Rarely', value: 2 },
              { text: 'Sometimes', value: 3 },
              { text: 'Often', value: 4 },
              { text: 'Always', value: 5 }
            ]
          },
          {
            text: 'How often do you feel anxious or worried?',
            options: [
              { text: 'Never', value: 1 },
              { text: 'Rarely', value: 2 },
              { text: 'Sometimes', value: 3 },
              { text: 'Often', value: 4 },
              { text: 'Always', value: 5 }
            ]
          },
          {
            text: 'How often do you have trouble concentrating?',
            options: [
              { text: 'Never', value: 1 },
              { text: 'Rarely', value: 2 },
              { text: 'Sometimes', value: 3 },
              { text: 'Often', value: 4 },
              { text: 'Always', value: 5 }
            ]
          },
          {
            text: 'How often do you feel overwhelmed by your responsibilities?',
            options: [
              { text: 'Never', value: 1 },
              { text: 'Rarely', value: 2 },
              { text: 'Sometimes', value: 3 },
              { text: 'Often', value: 4 },
              { text: 'Always', value: 5 }
            ]
          },
          {
            text: 'How often do you feel irritable or angry?',
            options: [
              { text: 'Never', value: 1 },
              { text: 'Rarely', value: 2 },
              { text: 'Sometimes', value: 3 },
              { text: 'Often', value: 4 },
              { text: 'Always', value: 5 }
            ]
          }
        ],
        answers: Array(5).fill(null),
        results: []
      };
    },
    methods: {
      calculateResults() {
        const conditions = {
          depression: 0,
          anxiety: 0,
          ADHD: 0,
          stress: 0,
          mood_disorder: 0
        };
  
        for (let i = 0; i < this.answers.length; i++) {
          if (i === 0) conditions.depression += parseInt(this.answers[i]);
          if (i === 1) conditions.anxiety += parseInt(this.answers[i]);
          if (i === 2) conditions.ADHD += parseInt(this.answers[i]);
          if (i === 3) conditions.stress += parseInt(this.answers[i]);
          if (i === 4) conditions.mood_disorder += parseInt(this.answers[i]);
        }
  
        const sortedConditions = Object.entries(conditions).sort((a, b) => b[1] - a[1]);
  
        this.results = sortedConditions.slice(0, 5).map(condition => ({
          name: condition[0].replace('_', ' '),
          score: condition[1]
        }));
      }
    }
  };
  </script>
  
  <style scoped>
  body {
    font-family: 'Raleway', sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
  }
  .container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  h1 {
    text-align: center;
  }
  .question {
    margin-bottom: 20px;
  }
  .result {
    margin-top: 20px;
    padding: 10px;
    background: #f9f9f9;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  }
  </style>
  