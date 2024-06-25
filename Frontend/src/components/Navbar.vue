<template>
  <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap" rel="stylesheet">
  <nav class="navbar is-transparent" style="background-color: #C1E1C1;" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="../img/logo2.png" alt="Logo">
      </a>
      <a role="button" class="navbar-burger" :class="{'is-active': isActive}" aria-label="menu" aria-expanded="false" @click="toggleMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" :class="{'is-active': isActive}" id="navMenu">
      <div class="navbar-start"></div>
      <div class="navbar-center">
        <router-link v-if="!token" class="navbar-item" to="/diagnosis">Diagnosis</router-link>
        <router-link v-if="!token" class="navbar-item" to="/forpractitioners">For Practitioners</router-link>
        <router-link v-if="!token" class="navbar-item" to="/findatherapist">Find A Therapist</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link v-if="!token" class="button has-background-success" to="/register">Doctor Register</router-link>
            <router-link v-if="!token" class="button has-background-warning" to="/login">Doctor Log in</router-link>
            <a @click="logout" v-if="token" class="button has-background-danger" to="/login">Log Out</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      isActive: false,
      token: localStorage.getItem('token')
    };
  },
  methods: {
    toggleMenu() {
      this.isActive = !this.isActive;
    },
    logout() {
      localStorage.clear();
      window.location = '/';
    }
  },
};
</script>

<style scoped>
.navbar {
  height: 100px;
  padding: 10px;
  font-family: 'Raleway', sans-serif;
  font-weight: 900;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-menu {
  display: flex;
  flex-grow: 1;
  justify-content: space-between;
  align-items: center;
}

.navbar-center {
  display: flex;
  justify-content: center;
  gap: 20px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.navbar-end {
  display: flex;
  align-items: center;
}
</style>
