<template>
  <div class="tour">
    <h2>A tour</h2>
    <div class="content">
      <v-btn icon>
        <v-icon class="paging">mdi-arrow-left-bold-circle</v-icon>
      </v-btn>
      <v-img class="img" src="https://picsum.photos/id/11/500/300"></v-img>
      <v-btn icon>
        <v-icon class="paging">mdi-arrow-right-bold-circle</v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      name: "",
      descriptions: []
    };
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

.paging {
}

.img {
  margin: 5rem;
  width: 35rem;
  height: 25rem;
}

.tour {
}
</style>