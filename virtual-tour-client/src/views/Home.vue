<template>
  <div class="home">
    <h1>Virtual Tour</h1>
    <div class="albums">
      <tour-overview
        v-for="(item, index) in albums"
        :key="item"
        :title="item"
        :id="albumIds[index]"
      />
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
      albums: [],
      albumIds: []
    };
  },
  created: async function() {
    const result = await Axios.get(
      "http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/albums"
    );
    this.albums = result.data["AlbumList"];
    this.albumIds = result.data["AlbumIndices"];
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

h1 {
  text-align: left;
}
</style>
