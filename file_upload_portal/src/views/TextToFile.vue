<template>
    <div id="container">
        <div id="textinput">
            <div>
                FN: <input type="text" v-model="filename"/>
            </div>
            <div style="margin: 10px 0 0 0;">
                <textarea v-model="body" rows="20" cols="36"></textarea>
            </div>       
            <div class="button-con">
                <button @click="addFile">Add File</button>
                <button @click="addFolder">Add Folder</button>
                <button @click="clear">Clear</button>
            </div>
        </div>
        <div id="fs-container">
            <div id="filetree">
                <fileTree :key="filetreeKey"/>
            </div>
            <div class="button-con" style="margin: 5px 0 0 0">
                <button @click="saveFile">Save</button>
                <button @click="reload">Reload</button>
            </div>            
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import fileTree from '@/components/FileTree.vue'
import { useStore } from 'vuex';


const store = useStore()
const filename = ref("")
const body = ref("")
const filetreeKey = ref(Date.now())

onMounted(async () => {
    await store.dispatch("getFS")
})

function saveFile() {
    let newFile = {
        name: filename.value,
        contents: body.value
    }
    console.log(newFile)
    store.state.currentFS.contents.push(newFile)
    store.dispatch("saveFS")
    
    filetreeKey.value = Date.now()

}

function addFile() {
    if (filename.value === "") {
        alert("Please enter a filename")
        return
    }
    if (store.state.currentFS.contents.filter(file => file.name === filename.value && file.type === "file").length > 0) {
        alert("File already exists")
        return
    }
    let newFile = {
        name: filename.value,
        type: "file",
        fileContents: body.value
    }
    store.state.currentFS.contents.push(newFile)
    filetreeKey.value = Date.now()
}

function addFolder() {
    if (filename.value === "") {
        alert("Please enter a folder name")
        return
    }
    if (store.state.currentFS.contents.filter(file => file.name === filename.value && file.type === "directory").length > 0) {
        alert("Folder already exists")
        return
    }
    if (body.value != "") {
        alert("Folders cannot have contents")
        return
    }
    let newFolder = {
        name: filename.value,
        type: "directory",
        contents: []
    }
    store.state.currentFS.contents.push(newFolder)
    filetreeKey.value = Date.now()
}

function clear() {
    filename.value = ""
    body.value = ""
}

async function reload() {
    await store.dispatch("getFS")
    filetreeKey.value = Date.now()
}

</script>

<style scoped>

#container {
    display: flex;
    justify-content: center;
}

#textinput {
    display: flex; 
    flex-direction: column;
    margin: 0 10px 0 0;
}

#filetree {
    width: 266px;
    border-style: solid;
    border-radius: 1%;
    border-width: thin;
    border-color: gray;
    padding: 10px;
}

#fs-container {
    display: flex;
    flex-direction: column;
}

.button-con {
    display: flex;
    justify-content: space-between;
}

</style>