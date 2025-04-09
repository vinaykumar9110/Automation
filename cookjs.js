document.getElementById('contact-form').addEventListener('submit', function(e) {
  e.preventDefault();

  // Simple form validation
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  if (name === '' || email === '' || message === '') {
    alert('Please fill in all fields.');
    return;
  }

  // Simulate form submission
  alert('Thank you for your message, ' + name + '!');

  // Reset form
  this.reset();
});

// Function to programmatically submit the form
function submitForm() {
  const form = document.getElementById('contact-form');
  form.requestSubmit(); // This will trigger the submit event listeners
}
