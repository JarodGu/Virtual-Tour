<template>
  <div class="home">
    <h2>Virtual Tour</h2>
    <div class="albums">
      <tour-overview v-for="item in albums" :key="item" :title="item" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TourOverview from "@/components/TourOverview.vue";
import Axios from "axios";

export default {
  name: "home",
  components: {
    TourOverview
  },
  data: function() {
    return {
      albums: []
    };
  },
  created: async function() {
    const result = await Axios.get(
      "http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/albums"
    );
    this.albums = result.data;
  }
};
</script>

<style scoped>
.home {
  padding: 1.5rem;
}

.albums {
  display: flex;
  flex-direction: row;
}
</style>
