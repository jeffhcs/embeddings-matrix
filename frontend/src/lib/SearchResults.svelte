<script>
    import Item from "./Item.svelte";
    export let results;
    export let weighted;
</script>

<main>
    <div class="title">
        {#if weighted}
            Composite
        {:else}
            Simple
        {/if}
        Embeddings
    </div>
    <div class="results">
        {#each results as item}
            <Item bind:item />
        {/each}
    </div>
</main>

<style>
    .results {
        display: flex;
        flex-direction: column;
        padding: 2em 1em;
        /* padding-top: 2em; */
        border: 2px solid var(--text);
        width: max(400px, 35vw);
        gap: 1em;
    }
    @media (max-width: 900px) {
        .results {
            width: 70vw;
        }
    }

    .title {
        padding-left: 0.5em;
        font-family: "Courier New", Courier, monospace;
        font-weight: bolder;
        font-size: 1.5em;
        margin-bottom: 0.5em;
    }
</style>
