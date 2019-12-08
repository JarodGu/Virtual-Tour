<template>
  <div class="tour">
    <h2>A tour</h2>
    <span>Description: {{ albumDescription }}</span>
    <div class="content" @click="switched()">
      <v-carousel v-model="model">
        <v-carousel-item v-for="(picture, i) in pictures" :key="i">
          <v-sheet height="100%" tile>
            <v-row class="fill-height" align="center" justify="center">
              <v-img class="img" :src="picture"></v-img>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
      <h2>Annotations</h2>
      <div v-for="annotation in currentAnnotations" :key="annotation">{{ annotation }}</div>
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
      albumDescription: "",
      descriptions: [],
      pictures: [],
      currentAnnotations: [],
      allAnnotations: [],
      model: 0
    };
  },
  methods: {
    switched: function() {
      this.currentAnnotations = this.allAnnotations[this.model];
    }
  },
  created: function() {
    const params = this.$route.params;
    Axios.get(
      `http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/album/?id=${params.id}`
    )
      .then(result => {
        console.log(result);
        this.pictures = result.data.images;
        this.albumDescription = result.data.AlbumDescription;

        const promises = [];
        this.pictures.forEach((picture, index) => {
          console.log(picture);
          promises.push(
            Axios.get(
              `http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/image?ImageID=${index}&AlbumID=${params.id}`
            )
          );
        });

        Promise.all(promises)
          .then(result => {
            console.log(result);
            result.forEach(result => {
              this.allAnnotations.push(result.data.Annotations);
              this.currentAnnotations = this.allAnnotations[this.model];
            });
          })
          .catch(error => {
            console.log(error);
          });
      })
      .catch(error => console.log(error));
  }
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
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