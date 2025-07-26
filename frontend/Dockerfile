# Dockerfile - formula-predictions-frontend
# =======================================================
# Formula Predictions frontend application.

FROM node:22-alpine

RUN apk add --no-cache curl

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1

CMD ["npm", "run", "start"]
