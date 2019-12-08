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

    <label>
      File
      <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
    </label>
    <button v-on:click="submitFile()">Submit</button>
    <v-text-field label="New Album Name" placeholder="New Album Name" v-model="newAlbumName"></v-text-field>
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
      albumIds: [],
      file: "",
      newAlbumName: ""
    };
  },
  methods: {
    handleFileUpload: function() {
      this.file = this.$refs.file.files[0];
    },
    submitFile: async function() {
      const formData = new FormData();
      console.log(this.file);
      formData.append("file", this.file);
      formData.append("albumName", this.newAlbumName);
      formData.append("fileName", this.file.name);
      const result = await Axios.post(
        "http://virtualtour-prod.kg3cdf3ppz.us-west-2.elasticbeanstalk.com/api/album",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );
    }
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
