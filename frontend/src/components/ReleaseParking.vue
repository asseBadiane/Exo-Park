=<template>
    <div>
      <label for="placeIdInput">Quelle place tu veux libérer? :</label>
      <input type="number" id="placeIdInput" v-model="inputPlaceId" />
      <button @click="releaseParking">Libérer la place </button>
      <div v-if="releasedPlaceId" style="margin: 20px;">Vous avez libéré la place {{ inputPlaceId }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        inputPlaceId: null, // Décommentez cette ligne pour initialiser inputPlaceId
        releasedPlaceId: null
      };
    },
    methods: {
      releaseParking() {
        axios.delete(`http://127.0.0.1:8000/parking/places/${this.inputPlaceId}`)
          .then(() => {
            this.releasedPlaceId = this.inputPlaceId;
            this.inputPlaceId = null; // Réinitialiser le champ d'entrée après la libération de la place
            this.$emit('released'); // Émettre un événement pour informer le composant parent que la place a été libérée
          })
          .catch(error => {
            console.error('Erreur lors de la libération de la place de parking:', error);
          });
      }
    }
  }
  </script>
  