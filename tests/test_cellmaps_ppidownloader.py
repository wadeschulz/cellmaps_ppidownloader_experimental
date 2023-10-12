#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cellmaps_imagedownloader` package."""

import os
import tempfile
import shutil

import unittest
from cellmaps_ppidownloader.runner import CellmapsPPIDownloader
from cellmaps_ppidownloader.exceptions import CellMapsPPIDownloaderError


class TestCellmapsDownloader(unittest.TestCase):
    """Tests for `cellmaps_imagedownloader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_run(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            run_dir = os.path.join(temp_dir, 'run')
            myobj = CellmapsPPIDownloader(outdir=run_dir)
            try:
                myobj.run()
                self.fail('Expected CellMapsImageDownloaderError')
            except CellMapsPPIDownloaderError as c:
                self.assertTrue('Invalid provenance' in str(c))
            self.assertFalse(os.path.isfile(os.path.join(run_dir, 'output.log')))
            self.assertFalse(os.path.isfile(os.path.join(run_dir, 'error.log')))
        finally:
            shutil.rmtree(temp_dir)

    def test_run_with_skip_logging_false(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            run_dir = os.path.join(temp_dir, 'run')
            myobj = CellmapsPPIDownloader(outdir=run_dir,
                                            skip_logging=False)
            try:
                myobj.run()
                self.fail('Expected CellMapsImageDownloaderError')
            except CellMapsPPIDownloaderError as c:
                self.assertTrue('Invalid provenance' in str(c))
            self.assertTrue(os.path.isfile(os.path.join(run_dir, 'output.log')))
            self.assertTrue(os.path.isfile(os.path.join(run_dir, 'error.log')))

        finally:
            shutil.rmtree(temp_dir)

