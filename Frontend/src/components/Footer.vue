<template>
    <footer class="footer">
      <div class="footer-container">
        <div class="footer-column">
          <img src="../img/LogoCropped.png" alt="Logo" class="footer-logo">
        </div>
        <div class="footer-column">
          <h3>COMPANY</h3>
          <ul>
            <li><a href="#">Our story</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Contact us</a></li>
            <li><a href="#">Press</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>DISCOVER</h3>
          <ul>
            <li><a href="#">Find a therapist</a></li>
            <li><a href="#">Search by location</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">For workplaces</a></li>
            <li><a href="#">Podcast</a></li>
            <li><a href="#">Sitemap</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>FOR PRACTITIONERS</h3>
          <ul>
            <li><a href="#">Get listed</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <div class="social-icons">
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-twitter"></i></a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-instagram"></i></a>
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-facebook"></i></a>
            <a href="https://youtube.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-youtube"></i></a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin"></i></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>If you are in a crisis and are looking for immediate help call <a href="tel:911">911</a> or see <a href="#">these resources</a>.</p>
        <p>Will probably need to add the address of the company here</p>
        <p><a href="#">Terms of service</a> | <a href="#">Privacy policy</a></p>
        <p>© 2024 The Waiting Room Inc</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer'
  };
  </script>
  
  <style scoped>
  .footer {
    background-color: #C1E1C1;
    color: #000000;
    padding: 40px 20px;
    font-family: 'Raleway', sans-serif;
    font-weight: 900;
  }
  
  .footer-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    max-width: 1200px;
    margin: auto;
  }
  
  .footer-column {
    flex: 1;
    min-width: 200px;
    margin: 20px;
  }
  
  .footer-column h3 {
    color: #000000;
    margin-bottom: 20px;
  }
  
  .footer-column ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-column ul li {
    margin-bottom: 10px;
  }
  
  .footer-column ul li a {
    color: #000000;
    text-decoration: none;
  }
  
  .footer-column ul li a:hover {
    text-decoration: underline;
  }
  
  .footer-logo {
    width: 150px;
  }
  
  .email-input {
    width: calc(100% - 40px);
    padding: 10px;
    margin-right: 10px;
    border: none;
    border-radius: 5px;
  }
  
  .submit-button {
    padding: 10px 20px;
    border: none;
    background-color: #C1E1C1;
    color: #000000;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .submit-button:hover {
    background-color: #C1E1C1;
  }
  
  .social-icons {
    margin-top: 20px;
  }
  
  .social-icons a {
    margin: 0 10px;
    color: #000000;
    font-size: 24px;
    text-decoration: none;
  }
  
  .footer-bottom {
    text-align: center;
    margin-top: 40px;
  }
  
  .footer-bottom p {
    margin: 10px 0;
  }
  
  .footer-bottom a {
    color: #000000;
    text-decoration: underline;
  }
  </style>
  