<script>
    export let item;

    $: weighted_terms = item.weighted_terms.map(t => `(${t[1]}) ${t[0]}`).join(", "); 
</script>

<main>
    <div class="left-block">

    <div class="count">{item.i}</div>
    
    <img src={item.image_url} alt={item.name} />
    </div>

    <div class="info">
        <p class="brand">{item.brand ? item.brand : "-"}</p>
        <p class="title">{item.name}</p>
        <!-- <p>Cosine Distance: <b>{item.wei.toFixed(4)}</b></p> -->
        <p class="distance">Simple Embedding: {item.unweighted_distance.toFixed(4)}</p>
        <div class="code-block">{item.unweighted_terms}</div>
        <p class="distance">Composite Embedding: {item.weighted_distance.toFixed(4)}</p>
        <div class="code-block">{weighted_terms}</div>
    </div>
</main>

<style>
    main {
        display: flex;
        gap: 1em;
        font-family: "Courier New", Courier, monospace;
        height: 12.5em;
        /* border: 2px solid #000; */
        /* padding: 1em; */
        padding-left: 0;
        width: 100%;
        box-sizing: border-box;
    }

    .count {
        font-size: 2em;
        text-align: right;
        /* margin-bottom: 0.5em; */
    }

    img {
        /* height: ; */
        /* width: 10em; */
        /* height: min(10em, 80%); */
        height: 6em;
    }

    .info {
        /* display: flex; */
        justify-content: space-between;
        width: 100%;
        /* flex-shrink: 1; */
        overflow: scroll;
    }

    p {
        margin-top: 0;
    margin-bottom: 0;
    }

    .brand {
        /* line-height: 0; */
        /* line-height: ; */
        font-size: 0.9em;
    }

    .title {
        font-size: 1.3em;
        /* line-height: 0em; */
        font-weight: bolder;
        /* margin-bottom: 0.5em; */
    }

    .distance {
        margin-top: 0.4em;
    }

    .code-block {
        background-color: #e0e0e0;
        color: #000;
        padding: 0.4em;
        border-radius: 4px;
        overflow-x: scroll;
        /* height: 1em; */
        /* white-space: nowrap; */
        width: 95%;
    }
</style>
