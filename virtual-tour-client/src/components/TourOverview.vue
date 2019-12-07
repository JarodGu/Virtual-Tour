<template>
  <div class="card" v-on:click="onNavigate()">
    <h3>{{ title }}</h3>
    <span>{{ albumInfo.AlbumDescription }}</span>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "TourOverview",
  props: ["title", "id"],
  data: () => {
    return {
      albumInfo: {
        AlbumDescription: ""
      }
    };
  },
  methods: {
    onNavigate: function() {
      this.$router.push(`/tour/${this.id}`);
    }
  },
  created: async function() {
    const result = await Axios.get(
      `http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/album/?id=${this.id}`
    );
    this.albumInfo = result.data;
    console.log(this.albumInfo);
  }
};
</script>

<style scoped>
.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 15rem;
  height: 15rem;
  padding: 1.5rem;
  margin: 1rem;
  border-radius: 10px; /* 5px rounded corners */
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>