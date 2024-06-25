<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>

  <section class="hero is-primary is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <h1 class="title has-text-centered animate__animated animate__fadeInDown">Welcome to The Waiting Room</h1>
        <p class="subtitle has-text-centered animate__animated animate__fadeIn">Diagnose, Discover, and Heal</p>
        <div class="columns is-multiline is-centered is-variable is-8">
          <div class="column is-narrow animate__animated animate__fadeInLeft">
            <RouterLink :to="'/diagnosis'">
              <div class="card has-text-centered">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img src="../img/diagnosis.png" style="object-fit: cover;" alt="Diagnosis">
                  </figure>
                </div>
                <header class="card-header">
                  <p class="card-header-title is-centered">Diagnosis</p>
                </header>
                <div class="card-content">
                  <div class="content">Figure out what mental health condition you may have.</div>
                </div>
              </div>
            </RouterLink>
          </div>

          <div class="column is-narrow animate__animated animate__fadeInLeft">
            <RouterLink :to="'/patients'">
              <div class="card has-text-centered">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img src="../img/doctor.jpg" style="object-fit: cover;" alt="Patients">
                  </figure>
                </div>
                <header class="card-header">
                  <p class="card-header-title is-centered">For Practitioners</p>
                </header>
                <div class="card-content">
                  <div class="content">Join our community to reach new clients.</div>
                </div>
              </div>
            </RouterLink>
          </div>

          <div class="column is-narrow animate__animated animate__fadeInUp">
            <RouterLink :to="'/calendar'">
              <div class="card has-text-centered">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img src="../img/appointment.jpg" style="object-fit: cover;" alt="Appointments">
                  </figure>
                </div>
                <header class="card-header">
                  <p class="card-header-title is-centered">Find A Therpist</p>
                </header>
                <div class="card-content">
                  <div class="content">Filter by location, specialization, and more.</div>
                </div>
              </div>
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      token: null,
    };
  },
  created() {
    this.token = localStorage.getItem("token");
  },
};
</script>

<style scoped>
.hero {
  background: linear-gradient(270deg, #84fab0, #8fd3f4, #a18cd1);
  background-size: 600% 600%;
  animation: Gradient 15s ease infinite;
  background-position: center;
}

@keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.card {
  width: 300px;
  overflow: hidden;
}

.card-image img {
  transition: transform 0.5s ease;
}

.card-image:hover img {
  transform: scale(1.05);
}

.container {
  overflow-x: hidden;
}

.card-image, .image {
  margin: 0;
}
</style>
