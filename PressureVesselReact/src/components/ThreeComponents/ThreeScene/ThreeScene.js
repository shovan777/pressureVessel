import React, { Component } from 'react';
import * as THREE from 'three';

class ThreeScene extends Component {
  componentDidMount() {
    const width = this.mount.clientWidth
    const height = this.mount.clientHeight

    // this.geometry = null;
    // this.material = null;
    // this.cylinder = null;
    //ADD SCENE
    this.scene = new THREE.Scene()

    //ADD CAMERA
    this.camera = new THREE.PerspectiveCamera(
      75,
      width / height,
      0.1,
      1000
    )
    this.camera.position.z = 4

    //ADD RENDERER
    this.renderer = new THREE.WebGLRenderer({ antialias: true })
    this.renderer.setClearColor('#ddd')
    this.renderer.setSize(width, height)
    this.mount.appendChild(this.renderer.domElement)

    //ADD LIGHT
    this.light = new THREE.AmbientLight(0x404040); // soft white light
    this.scene.add(this.light);

    this.directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    this.directionalLight.position.set(0, -70, 100).normalize()

    //ADD GEOMETRY
    this.geometry = new THREE.SphereGeometry(1, 64, 64, 0, 6.3, 0, 1.5);
    this.material = new THREE.MeshBasicMaterial({ color: '#999' });
    this.sphere = new THREE.Mesh(this.geometry, this.material);
    // this.sphere.translateY(0.93);
    this.scene.add(this.sphere)

    // this.geometry = new THREE.BoxGeometry( 1, 1, 1 );
    // this.material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    // this.cube = new THREE.Mesh( this.geometry, this.material );
    // this.scene.add( this.cube );  

    // this.geometry = new THREE.CylinderGeometry(1, 1, 2, 32,32,true,0,6.3)
    // this.material = new THREE.MeshBasicMaterial({ color: '#777' })
    // this.cylinder = new THREE.Mesh(this.geometry, this.material)
    // this.scene.add(this.cylinder)
    this.start()

    console.log("ComponentDidMount ThreeScene");
  }

  componentWillUnmount() {
    console.log("ComponentWillUnmount ThreeScene");
  }

  componentWillReceiveProps(nextProps) {
    console.log("ComponentWillReceiveProps ThreeScene ");
    console.log(nextProps.length);
    const l = nextProps.length;
    if (l > 0 && nextProps.length !== this.props.length) {
      console.log(" Inside ComponentWillReceiveProps ThreeScene ");
      //this.stop()
      this.geometry = new THREE.CylinderGeometry(1, 1, 2, 32, 32, true, 0, 6.3)
      this.material = new THREE.MeshBasicMaterial({ color: '#777' })
      this.cylinder = new THREE.Mesh(this.geometry, this.material)
      this.scene.add(this.cylinder)
      this.sphere.translateY(0.93);
      this.start()
    }
  }
  start = () => {
    if (!this.frameId) {
      this.frameId = requestAnimationFrame(this.animate)
    }
  }

  stop = () => {
    cancelAnimationFrame(this.frameId)
  }

  animate = () => {
    if (this.cube != null) {
      this.cube.rotation.x += 0.01
      this.cube.rotation.y += 0.01
    }
    // this.cylinder.rotation.x += 0.01
    // this.cylinder.rotation.y += 0.01
    this.renderScene()
    this.frameId = window.requestAnimationFrame(this.animate)
  }

  renderScene = () => {
    this.renderer.render(this.scene, this.camera)
  }

  render() {
    return (
      <div
        style={{ width: '100%', height: '600px' }}
        ref={(mount) => { this.mount = mount }}
      />
    )
  }
}

export default ThreeScene