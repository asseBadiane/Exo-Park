<template>
  <div>
    <h2>Voici la liste des Places de Parking</h2>
    <ul>
      <li v-for="place in places" :key="place.id">
       Place {{ place.numero }} - {{ place.occupee ? "Occupée" : "Libre" }}
      </li>
      
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      places: [],
    };
  },
  created() {
    this.fetchPlaces();
  },
  methods: {
    fetchPlaces() {
      axios
        .get("/")
        .then((response) => {
          this.places = response.data;
        })
        .catch((error) => {
          console.error(
            "Erreur lors de la récupération des places de parking:",
            error
          );
        });
    },
  },
};
</script>
