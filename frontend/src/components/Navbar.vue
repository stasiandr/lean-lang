<template>
  <v-navigation-drawer
    :value="menuIsOpened"
    @input="setMenuOpened"
    app
    class="primary"
  >
    <v-row class="mt-5" justify="center" align="center">
      <v-col cols="6">
        <v-avatar size="100">
          <img :src="user.profile_pic" v-if="'profile_pic' in user" />
          <span class="white--text text-h5" v-else>{{
            user.first_name[0] + user.last_name[0]
          }}</span>
        </v-avatar>
        <p class="white--text subtitle-1 mt-2 text-center">
          {{ user.first_name }} {{ user.last_name }}
        </p>
      </v-col>
    </v-row>
    <v-list nav dense>
      <v-list-item
        link
        v-for="link in links"
        :key="link.text"
        router
        :to="link.route"
      >
        <v-list-item-icon>
          <v-icon class="white--text">{{ link.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-title class="white--text">{{
          link.text
        }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data() {
    return {
      links: [
        { icon: 'mdi-view-dashboard', text: 'Tasks', route: '/tasks' },
        { icon: 'mdi-book-variant', text: 'Classroom', route: '/classroom' },
        { icon: 'mdi-account', text: 'Account', route: '/account' },
      ],
    }
  },
  computed: {
    ...mapGetters('auth', ['user']),
    ...mapGetters('modal', ['menuIsOpened']),
  },
  methods: {
    ...mapActions('modal', ['setMenuOpened']),
  },
}
</script>
