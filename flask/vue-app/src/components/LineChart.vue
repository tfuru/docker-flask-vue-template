<script lang="ts">
import { Component, Prop, Mixins } from 'vue-property-decorator';

import Chart from "chart.js";
import { Line, Bar, mixins } from "vue-chartjs";

@Component({
  components: {
    Line
  }
})
export default class LineChart extends Mixins(Line, Bar, mixins.reactiveProp) {
  @Prop() public chartData!: Chart.ChartData;
  @Prop() public chartOptions!: Chart.ChartOptions;

  public mounted() {
    console.log(this);
    this.renderChart(this.chartData!, this.chartOptions!);
  }
}
</script>

<style lang="scss">

</style>
