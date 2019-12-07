<template>
  <div class="tour">
    <h2>A tour</h2>
    <div class="content">
      <v-carousel>
        <v-carousel-item v-for="(picture, i) in pictures" :key="i">
          <v-sheet :color="color" height="100%" tile>
            <v-row class="fill-height" align="center" justify="center">
              <v-img class="img" :src="picture"></v-img>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>

      <!-- <v-btn icon>
        <v-icon class="paging">mdi-arrow-left-bold-circle</v-icon>
      </v-btn>
      <v-img class="img" src="https://picsum.photos/id/11/500/300"></v-img>
      <v-btn icon>
        <v-icon class="paging">mdi-arrow-right-bold-circle</v-icon>
      </v-btn>-->
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  data: () => {
    return {
      name: "",
      descriptions: [],
      pictures: []
    };
  },
  created: function() {
    const params = this.$route.params;
    Axios.get(
      `http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/album/?id=${params.id}`
    )
      .then(result => {
        console.log(result);
        this.pictures = result.data;
      })
      .catch(error => console.log(error));
  }
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.img {
  margin: 5rem;
  width: 35rem;
  height: 25rem;
}

h2 {
  margin-bottom: 1rem;
}
</style>