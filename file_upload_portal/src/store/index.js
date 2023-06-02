import { createStore } from 'vuex'
import axios from 'axios'
import { isValidJwt } from '@/utils'


export default createStore({
  state: {
    blankPassword: false,
    failedAuthErr: undefined,
    jwt: null,
    loginSuccess: false,
    currentFS: {},
  },
  getters: {
    isAuthenticated(state) {
      return isValidJwt(state.jwt)
    }
  },
  mutations: {
    setCurrentFS(state, payload) {
      state.currentFS = payload
    },
    setJwtToken(state, payload) {
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    },
    setFailedAuthentication(state, payload) {
      state.failedAuthErr = payload
    },
    setFailedTreeGet(state, payload) {
      state.failedTreeGet = payload
    },
    setLoginSuccess(state) {
      state.loginSuccess = true
    }
  },
  actions: {
    async login({ commit }, payload) {
      try {
        const res = await axios.post("/api/login", payload)

        commit("setJwtToken", {jwt: res.data.token})
        commit("setLoginSuccess")
      } catch (err) {
        commit("setFailedAuthentication", err)
      }
    },
    async saveFS({state}) {
      try {
        await axios.post("/api/fs", state.store.currentFS)
      } catch (err) {
        console.log(err)
      }
    },
    async getFS({ commit }) {
      try {
        const res = await axios.get("/api/fs")
        commit("setCurrentFS", res.data.fs)

      } catch (err) {
        commit("setFailedTreeGet", err)
      }
    }, 
    async saveFiles(_, payload) {
      try {
        let formData = new FormData()
        for (let file of payload) {
          formData.append('file', file)
        }
        await axios.post("/api/files/save", formData, {headers: {'Content-Type': 'multipart/form-data'}})
      } catch (err) {
        console.log(err)
      }
    }
  }
})
