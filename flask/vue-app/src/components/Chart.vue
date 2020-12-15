<template>
  <div class="Chart">
    <h1>Chart</h1>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Chart extends Vue {
    @Prop() 
    private data!: any[];
}
</script>

<style lang="scss">

</style>
