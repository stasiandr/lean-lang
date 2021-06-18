<template>
  <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col col="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Registration form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-account"
                id="username"
                name="username"
                label="Username"
                type="text"
                v-model="data.username"
              ></v-text-field>
              <v-text-field
                id="email"
                name="email"
                prepend-icon="mdi-email"
                label="Email"
                type="email"
                v-model="data.email"
              ></v-text-field>
              <v-text-field
                id="first_name"
                name="first_name"
                label="First name"
                type="text"
                v-model="data.first_name"
              ></v-text-field>
              <v-text-field
                id="last_name"
                name="email"
                label="Last name"
                type="text"
                v-model="data.last_name"
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="data.password"
              ></v-text-field>
              <v-text-field
                id="re_password"
                prepend-icon="mdi-lock"
                name="re_password"
                label="Re-enter password"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="register(data)">Register</v-btn>
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
      data: {
        username: '',
        email: '',
        password: '',
        first_name: '',
        last_name: '',
      },
    }
  },
  methods: {
    ...mapActions('auth', ['register']),
  },
}
</script>

<style></style>
