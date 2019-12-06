<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <span>Some sort of tour description</span>
  </div>
</template>

<script>
export default {
  name: "TourOverview",
  props: ["title"]
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