<script>
  import { Content, Grid } from "carbon-components-svelte";
  import Theme from "../components/Theme.svelte";
  import Navigation from "./_navigation.svelte";
</script>

<Theme persist theme="g100">
  <Navigation />
  <Content style="background: none; padding: 1rem">
    <Grid>
      <slot />
    </Grid>
  </Content>
</Theme>
