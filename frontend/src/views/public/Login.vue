<template>
  <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col col="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                id="email"
                prepend-icon="mdi-account"
                name="email"
                label="Email"
                type="text"
                v-model="credentials.email"
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="credentials.password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="login(credentials)">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      credentials: {
        email: '',
        password: '',
      },
    }
  },
  methods: {
    ...mapActions('auth', ['login']),
  },
}
</script>
