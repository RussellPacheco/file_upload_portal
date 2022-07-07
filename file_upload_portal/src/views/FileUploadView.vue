<template>
    <div class="file-upload" @dragover.prevent @drop.prevent>
        <h1 id="title">File Upload</h1>
        <div class="container">
            <div class="col"></div>
            <div class="col">
                <input id="input" type="file" multiple @change="fileUpload" />
                <div id="drop-area" @drop="drop">
                    <div class="row"></div>
                    <div class="row mid">
                        <span class="label large">DROP HERE</span>
                    </div>
                    <div class="row"></div>
                </div>
            </div>
            <div class="col">
                <div v-if="fileUploaded">
                    <div id="col-three">
                        <h3>File(s) to be uploaded:</h3>
                        <div class="container col" v-for="(file, index) in files" :key="index">
                            <div class="container">
                                <div class="label">Name:</div>
                                <div>{{file.name}}</div>
                            </div>
                            <div class="container">
                                <div class="label">Size:</div>
                                <div>{{fileSizeFormatter(file.size, 1)}} {{fileSizeFormatter(file.size, 2)}}</div>
                            </div>
                        </div>
                    </div>
                    <div class="container inner">
                        <button class="button" @click="saveFiles">Submit</button>
                        <button class="button" @click="clearFiles">Clear</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "FileUploadView",
    data () {
        return {
            files: [],
            fileUploaded: false
        }  
    },
    methods: {
        drop(e) {
            this.files = e.dataTransfer.files
            this.fileUploaded = true
        },
        fileUpload(e) {
            this.files = e.target.files
            this.fileUploaded = true
        },
        clearFiles() {
            this.files = []
            this.fileUploaded = false
        },
        saveFiles() {
            console.log(this.files)
            this.$store.dispatch("saveFiles", this.files)
        },
        fileSizeFormatter(size, position) {
            if (position == 1) {
                if (size < 1024) {
                    return size
                }
                if (size / 1024 < 1024) {
                    return size / 1024
                }
                if (size / 1024 / 1024 < 1024) {
                    return size / 1024 / 1024
                }
            } else {
                if (size < 1024) {
                    return "bytes"
                }
                if (size / 1024 < 1024) {
                    return "KB"
                }
                if (size / 1024 / 1024 < 1024) {
                    return "MB"
                }
            }
        }
    }

}

</script>

<style scoped>

.container {
    display: flex;
}

.container.col{
    flex-direction: column;
    justify-content: space-between;
    width: 200px;
    margin-left: 15%;
}
.container.inner {
    padding-top: 5%;
    margin-right: 7%;
    justify-content: end;
}

.label {
    font-weight: bold;
}

.label.large {
    font-size: 40px;
    opacity: 50%;

}

#title {
    margin-right: 5%;
}
.col {
    width: 29%
}

.row {
    width: 29%
}

.row.mid {
    margin-top: 27%;
    margin-left: 5%;
}

#col-three {
    margin-left: 45%;
}

#drop-area {
    background: #dbdbd9;
    border-style: dashed;
    width: 500px;
    height: 400px;
    text-align: center;
    display: flex;
}

#input {
    margin-left: 42%;
    padding-bottom: 1%;
}

button {
    margin: 5%;
}
</style>