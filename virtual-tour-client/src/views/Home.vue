<template>
  <div class="home">
    <h2>Virtual Tour</h2>
    <tour-overview />
  </div>
</template>

<script>
// @ is an alias to /src
import TourOverview from "@/components/TourOverview.vue";

export default {
  name: "home",
  components: {
    TourOverview
  }
};
</script>

<style scoped>
.home {
  padding: 1.5rem;
}
</style>
