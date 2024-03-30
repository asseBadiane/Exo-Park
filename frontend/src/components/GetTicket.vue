<template>
  <div>
    <h2>Obtenir un ticket de parking</h2>
    <form @submit.prevent="submitTicket">
      <label for="placeNumber">Quelle place tu veux garer dans le parking :</label>
      <input type="number" id="placeNumber" v-model="placeNumber" required />
      <button type="submit">Obtenir un ticket</button>
    </form>
    <p v-if="message">Vous avez obtenu le ticket de parking sur la place {{ placeNumber }}</p>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      placeNumber: null,
      message: ''
    };
  },
 
  methods: {
    
  submitTicket() {
    axios.post('/', { numero: this.placeNumber })
      .then(() => {
        this.message = 'Ticket de parking créé avec succès !';
      })
      .catch(error => {
        if (error.response) {
          this.message = error.response.data.detail || 'Erreur lors de la création du ticket de parking.';
        } else {
          this.message = 'Erreur lors de la création du ticket de parking : ' + error.message;
        }
        console.error('Erreur lors de la création du ticket de parking :', error);
      });
  }
}

}
</script>
