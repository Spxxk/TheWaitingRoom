<template>
    <section class="hero">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-vcentered">
            <div class="column is-half">
              <h1 class="title">Grow your private practice, your way.</h1>
              <p class="subtitle">
                Connect with committed clients. Join our community of private practice owners. No marketing skills required.
              </p>
              <button class="button is-dark">Partner with us</button>
            </div>
            <div class="column is-half">
              <figure class="image is-4by3">
                <img src="../img/Practitioner.jpg" alt="Practitioner">
              </figure>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'ForPractitioners'
  };
  </script>
  
  <style scoped>
  .hero {
    background-color: #E3F2FD;
    padding: 3rem 1.5rem;
  }
  
  .hero .title {
    font-size: 3rem;
    font-weight: 900;
    color: #333;
  }
  
  .hero .subtitle {
    font-size: 1.5rem;
    margin-top: 1rem;
    color: #555;
  }
  
  .button.is-dark {
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    margin-top: 2rem;
    cursor: pointer;
  }
  
  .button.is-dark:hover {
    background-color: #555;
  }
  </style>
  